import React, { useState } from 'react';

const QueuePanel = () => {
    const [files, setFiles] = useState([]);
    const [uploadQueue, setUploadQueue] = useState([]);

    const handleFileChange = (event) => {
        setFiles(event.target.files);
    };

    const handleUpload = () => {
        const newUploads = Array.from(files);
        setUploadQueue([...uploadQueue, ...newUploads]);
        setFiles([]);
    };

    return (
        <div>
            <h2>File Upload and Queue Display</h2>
            <input type="file" multiple onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload Files</button>
            <h3>Upload Queue</h3>
            <ul>
                {uploadQueue.map((file, index) => (
                    <li key={index}>{file.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default QueuePanel;