import React from 'react';

const DocumentViewer = ({ document }) => {
    return (
        <div className="document-viewer">
            <h2>Document Preview</h2>
            <iframe 
                src={document} 
                title="Document Viewer" 
                width="100%" 
                height="600px"
                frameBorder="0"
            ></iframe>
        </div>
    );
};

export default DocumentViewer;