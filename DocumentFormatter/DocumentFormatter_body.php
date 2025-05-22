<?php
if ( !defined( 'MEDIAWIKI' ) ) {
    die( -1 );
}

namespace MediaWiki\Extension\DocumentFormatter;

use SpecialPage;
use HtmlForm\FormFactory;
use HtmlForm\SpecialFormContext;

class SpecialDocumentFormatter extends \SpecialPage {
    public function __construct() {
        parent::__construct( 'documentformatter' );
        $this->mListed     = true;
        $this->mIncludable = false;
    }

    public function execute( $par ) {
        $out = $this->getOutput();
        $this->setHeaders();
        $out->setPageTitle( 'Document Formatter' );

        // 1) Define your form fields
        $formDescriptor = [
            'page' => [
                'label'    => 'Select a Page',
                'type'     => 'title',
                'id'       => 'page',
                'required' => true,
            ],

            'file' => [
                'label'       => 'Upload your source document',
                'type'        => 'file',
                'id'          => 'file',
                'help'        => 'Choose a .docx or .txt file to format',
                'required'    => false,
            ],

            'filetype' => [
                'label'    => 'What format was your file originally in?',
                'type'     => 'radio',
                'options'  => [
                    'Word'    => 0,
                    'Outline' => 1,
                ],
                'id'       => 'type',
                'required' => true,
            ],
        ];

        // 2) Build the HtmlForm
        $htmlForm = FormFactory::getForm(
            'documentformatter-form',  // unique form ID
            $formDescriptor,           // your fields
            $this,                     // handler object
            'processInput'             // callback method
        );

        // 3) Enable file uploads
        $htmlForm->setMethod( 'post' );
        $htmlForm->setEnctype( 'multipart/form-data' );

        // 4) Customize and show
        $htmlForm->setSubmitText( 'Run Formatter' );
        $htmlForm->show();

        // Stop further output
        return;
    }

    public static function processInput( SpecialFormContext $context ) {
        $request  = $context->getRequest();
        $formData = $request->getValues();

        // Handle upload (if provided)
        $upload = $request->getUpload( 'file' );
        if ( $upload && $upload->isOk() ) {
            $IP      = str_ireplace( '/extensions/DocumentFormatter', '', __DIR__ );
            $dest    = "$IP/images/" . $upload->getLocalName();
            $upload->moveTo( $dest );
            $filedir = $dest;
        } else {
            // Fallback: find by name
            $filedir = exec( "find $IP/images -name '{$formData['file']}'" );
        }

        // Your existing logic to call the Python script
        $dir     = __DIR__;
        $page    = str_replace( ' ', '_', $formData['page'] );
        $type    = $formData['filetype'];
        $command = "cd $dir/resources/python && pwb login && python3 variables.py "
                 . escapeshellarg( $dir ) . ' '
                 . escapeshellarg( $page ) . ' '
                 . escapeshellarg( $filedir ) . ' '
                 . escapeshellarg( $type );
        $output  = shell_exec( $command );

        // Display the result back to the user
        $context->getOutput()->addWikiTextAsContent(
            "=== Formatter Result ===\n<pre>" . htmlspecialchars( $output ) . "</pre>"
        );
    }

    protected function getGroupName() {
        return 'other';
    }
}
