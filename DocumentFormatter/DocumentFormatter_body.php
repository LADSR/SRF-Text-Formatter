<?php
/**
 * Necessary description of @file, @authors and license
 * @FILLME!
 * Always good to remind that important part
 */
 
if ( !defined( 'MEDIAWIKI' ) ) { 
	die( -1 ); 
}

$dir = __DIR__ . '/'; 

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
		$out = $this->getOutput();
        $this->setHeaders();
        //Page Layout
        $out->setPageTitle( 'Document Formatter' );
        $formDescriptor = [
            'page' => [
                //'cssclass' => ''
                'label' => 'Select a Page',
                'type' => 'text',
                'id' => 'page',
                'required' => true
            ],

            'file' => [
                //'cssclass' => ''
                'label' => 'Paste the name of your word document',
                'type' => 'text',
                'id' => 'file'
            ],

            'filetype' => [
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
        $htmlForm->setFormIdentifier( 'form' );
    }
   
    ///Logic
    public static function processInput( $formData ) {
        $page = $formData['page'];
        $file = $formData['file'];
        $filedir = exec("find /var/www/vhosts/wiki.ontracknorthamerica.org/httpdocs/images/ -name '$file'");
        $filetype = $formData['filetype'];
        
        $command = "cd /var/www/vhosts/wiki.ontracknorthamerica.org/httpdocs/extensions/DocumentFormatter/resources/python && pwb login && python3 variables.py $page $filedir $filetype";
        exec($command . " 2>&1", $output);
        var_dump($output);
    }

    protected function getGroupName() {
        return 'other';
    }
}