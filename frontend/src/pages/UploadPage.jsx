import React, { useState } from "react";
import { Button } from "@/components/ui/button";

const UploadPage = () => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleDrop = (event) => {
        event.preventDefault();
        setSelectedFile(event.dataTransfer.files[0]);
    };

    const handleExport = () => {
        if (selectedFile) {
            alert(`Exporting report for: ${selectedFile.name}`);
            // Implement actual report export functionality
        } else {
            alert("No file selected to export.");
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-8">
            <h2 className="text-3xl font-semibold mb-4">Upload Your Image</h2>
            <div
                className="border-2 border-dashed border-gray-400 p-6 w-96 h-40 flex items-center justify-center cursor-pointer"
                onDragOver={(e) => e.preventDefault()}
                onDrop={handleDrop}
            >
                {selectedFile ? (
                    <p className="text-green-500">{selectedFile.name}</p>
                ) : (
                    <p className="text-gray-500">Drag & drop an image here or click to select</p>
                )}
            </div>
            <input type="file" className="hidden" id="file-input" onChange={handleFileChange} />
            <label
                htmlFor="file-input"
                className="mt-4 bg-blue-500 text-white px-4 py-2 rounded cursor-pointer hover:bg-blue-600"
            >
                Select File
            </label>

            <Button onClick={handleExport} className="mt-4 px-6 py-3 bg-green-500 text-white rounded-lg shadow-lg hover:bg-green-600">
                Export Report
            </Button>
        </div>
    );
};

export default UploadPage;
