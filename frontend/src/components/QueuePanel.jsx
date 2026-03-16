import React, { useRef } from 'react';
import api from '../api';

export default function QueuePanel({ queue, setQueue }) {
  const fileInputRef = useRef();
  const handleUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);
    try {
      const res = await api.post('/upload', formData);
      setQueue([...queue, res.data]);
    } catch (e) {
      alert('Upload failed');
    }
  };
  return (
    <div>
      <input ref={fileInputRef} type="file" onChange={handleUpload} />
      {/* ...rest of UI */}
    </div>
  );
}