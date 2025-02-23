document.addEventListener("DOMContentLoaded", function () {
    const dropArea = document.getElementById("drop-area");
    const fileInput = document.getElementById("file-input");
    const exportBtn = document.getElementById("export-btn");
    let selectedFile = null;

    dropArea.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropArea.classList.add("drag-over");
    });

    dropArea.addEventListener("dragleave", () => {
        dropArea.classList.remove("drag-over");
    });

    dropArea.addEventListener("drop", (e) => {
        e.preventDefault();
        dropArea.classList.remove("drag-over");
        selectedFile = e.dataTransfer.files[0];
        alert("File Uploaded: " + selectedFile.name);
    });

    fileInput.addEventListener("change", () => {
        selectedFile = fileInput.files[0];
        alert("File Uploaded: " + selectedFile.name);
    });

    exportBtn.addEventListener("click", () => {
        if (selectedFile) {
            generateReport(selectedFile.name);
        } else {
            alert("No file selected to export.");
        }
    });

    function generateReport(fileName) {
        const reportContent = `AI Image Analysis Report\n\nFile Name: ${fileName}\nStatus: Analysis Completed\nResult: No issues detected (Example)`;

        const blob = new Blob([reportContent], { type: "text/plain" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "AI_Report.txt";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }
});
