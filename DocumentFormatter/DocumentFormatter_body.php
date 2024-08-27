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

    /*Extensions Layout*/
    public function execute( $par ) {
		$out = $this->getOutput();
        $this->setHeaders();
        $out->setPageTitle( 'Document Formatter' );

        $formDescriptor = [
            'Namespace' => [
                'label' => 'Select a Page',
                'type' => 'namespaceselect',
            ],
            'page' => [
                'label' => 'Select a Page',
                'type' => 'title',
                'id' => 'page',
                'required' => true
            ],
            'file' => [
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
            ],

            #Optional Extra Formating Options
            'color' => [
                'label' => 'Use Word Document Text Colors',
                'type' => 'check'
            ]
        ];
        
        $htmlForm = HTMLForm::factory( 'table', $formDescriptor, $this->getContext() );
        $htmlForm->setSubmitText( 'Save' );
        $htmlForm->setSubmitCallback( [ $this, 'processInput' ] );
        $htmlForm->show();
        $htmlForm->setFormIdentifier( 'form' );
    }

    /*Extension Logic*/
    public static function processInput( $formData ) {
        $dir = __DIR__;
        $IP = str_ireplace("/extensions/DocumentFormatter", "", $dir);
        
        #Select from list of pages / create a page
        $page = $formData['page'];
        if (str_contains($page, " ")) {
            $page = str_ireplace(" ", "_", $page);
            print_r($page);
        }

        $file = $formData['file'];
        if (str_contains($file, " ")){
            $file = str_ireplace(" ", "_", $file);
            print_r($file);
        }

        $filedir = exec("find $IP/images -name '$file'");
        $filetype = $formData['filetype'];
        
        $color = $formData['color'];

        #$command = "cd $dir/resources/python && pwb login && python3 variables.py $dir $page $filedir $filetype $color";
        #exec($command . " 2>&1", $output);
        #var_dump($output);
    }

    protected function getGroupName() {
        return 'other';
    }
}