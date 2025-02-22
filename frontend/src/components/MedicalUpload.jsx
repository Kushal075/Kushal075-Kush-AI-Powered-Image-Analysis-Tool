import React, { useState } from 'react';
import axios from 'axios';

const MedicalUpload = () => {
    const [file, setFile] = useState(null);
    const [prediction, setPrediction] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('file', file);

        const response = await axios.post('/api/medical/predict', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });

        setPrediction(response.data.prediction);
    };

    return (
        <div>
            <h2>Upload Medical Image</h2>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} />
                <button type="submit">Upload</button>
            </form>
            {prediction && <p>Prediction: {prediction}</p>}
        </div>
    );
};

export default MedicalUpload;
