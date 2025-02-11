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

    public function execute( $par ){
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
        #$this->getOutput()->addHTML( '<big>Instructions</big><\br>Step 1: Create or Choose a Page</br> Step 2: Upload your file to the wiki</br> Step 3: Fill out Short form on special Page and Submit' );
        
        $htmlForm = HTMLForm::factory( 'table', $formDescriptor, $this->getContext() );
        $htmlForm->setSubmitText( 'Save' );
        $htmlForm->setSubmitCallback( [ $this, 'processInput' ] );  
        $htmlForm->show();
        $htmlForm->setFormIdentifier( 'form' );
    }
    
    ///Logic
    public static function processInput( $formData ) {
        $dir = __DIR__;
        $IP = str_ireplace("/extensions/DocumentFormatter", "", $dir);
        #Select from list of pages / create a page
        $page = $formData['page'];
        if (str_contains($page, " ")) {
            $page = str_ireplace(" ", "_", $page);
        }

        $file = $formData['file'];
        if (str_contains($file, " ")){
            $file = str_ireplace(" ", "_", $file);
        }

        $filedir = exec("find $IP/images -name '$file'");
        $filetype = $formData['filetype'];

        $command = "cd $dir/resources/python && pwb login && python3 variables.py $dir $page $filedir $filetype";
        $output = shell_exec($command);
        var_dump($output);
        #exec($command . " 2>&1 &", $output);
    }

    protected function getGroupName() {
        return 'other';
    }
}