<?php
/**
 * Necessary description of @file, @authors and license
 * @FILLME!
 * Always good to remind that important part
 */
 
if ( !defined( 'MEDIAWIKI' ) ) { 
	die( -1 ); 
}


class SpecialDocumentFormatter extends \SpecialPage {
    public function __construct() {
        parent::__construct( 'documentformatter' );
        $this->mListed = true;
        $this->mIncludable = false;
    }
    /**
     * Special page entry point
     * @param string|null $par
     */

    public function execute( $par ) {
        //$request = $this->getRequest();
		$out = $this->getOutput();
        $this->setHeaders();
        //Page Layout
        $out->setPageTitle( 'Document Formatter' );
        $formDescriptor = [
            
            'page' => [
                //'cssclass' => ''
                'label' => 'Select a Page',
                'type' => 'title',
                'id' => 'page',
                'required' => true
            ],
            'file' => [
                //'cssclass' => ''
                'label' => 'Upload a Word Document',
                'type' => 'file',
                'id' => 'file',
                'required' => true
            ],

            'filetype' => [
                //'default' => '',
                //'cssclass' => ''
                'label' => 'What format was your file originally in?',
                'type' => 'radio',
                'options' => [
                    'Word' => 0,
                    'Outline' => 1
                ],
                'id' => 'type',
                'required' => true
            ]
        ];

        
        $htmlForm = HTMLForm::factory( 'table', $formDescriptor, $this->getContext() );
        $htmlForm->setSubmitText( 'Save' );
        $htmlForm->setSubmitCallback( [ $this, 'processInput' ] );  
        $htmlForm->show();
        $htmlForm->setFormIdentifier( 'myform1' );
    }

    ///Logic
    public static function processInput( $formData, $out) {
        if ($formData['page'] === ''){
            return false;
        }else{
            $page = $formData['page'];
        }
        
        if ($formData['file'] === ''){
            return false;
        }else{
            $file = $formData['file'];
        }
        
        if ($formData['filetype'] === ''){
            return false;
        }else{
            $filetype = $formData['filetype'];
            
            $command = escapeshellcmd("python3 /var/www/vhosts/wiki.strategicrail.com/httpdocs/extensions/DocumentFormatter/resources/python/variables.py $page $file $filetype");
            exec($command, $output);
            $command1 = escapeshellcmd("python3 /var/www/vhosts/wiki.strategicrail.com/httpdocs/extensions/DocumentFormatter/resources/python/main.py");
            exec($command1, $output);

            print_r($output[1]);
        }
    }

    protected function getGroupName() {
        return 'other';
    }
}