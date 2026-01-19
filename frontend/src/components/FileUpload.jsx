import axios from "axios";
import { useState } from "react";
import { JsonView } from "react-json-view-lite";
import "react-json-view-lite/dist/index.css";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileSelect = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
    setError("");
  };

  const handleAnalyze = async () => {
    if (!file) {
      setError("Please select a log file first!");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const formData = new FormData();
      formData.append("logFile", file);

      const res = await axios.post(
        "https://ai-integrated-log-analyzer.onrender.com/api/logs/analyze",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );


      console.log("RAW RESPONSE:", res.data);

      let cleaned = res.data.analysis
        .replace(/```json/g, "")
        .replace(/```/g, "")
        .trim();

      console.log("CLEANED JSON:", cleaned);

      setResult(JSON.parse(cleaned));
      } catch (err) {
        setError("Failed to analyze log file.");
        console.error(err);
      }

    setLoading(false);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Log Analyzer</h2>

      {/* Select File */}
      <input type="file" onChange={handleFileSelect} />

      {file && <p>Selected File: <strong>{file.name}</strong></p>}

      {/* Analyze Button */}
      <button 
        onClick={handleAnalyze}
        style={{
          marginTop: "10px",
          padding: "8px 16px",
          cursor: "pointer"
        }}
      >
        {loading ? "Analyzing..." : "Analyze Log"}
      </button>

      {/* Error */}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Result */}
      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Analysis Result:</h3>
          <JsonView data={result} />
        </div>
      )}
    </div>
  );
};

export default FileUpload;
