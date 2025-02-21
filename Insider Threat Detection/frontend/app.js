import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
    const [logs, setLogs] = useState([]);
    
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/logs").then(response => {
            setLogs(response.data.logs);
        });
    }, []);
    
    return (
        <div>
            <h1>Insider Threat Logs</h1>
            <table>
                <thead>
                    <tr>
                        <th>User ID</th>
                        <th>Threat Status</th>
                    </tr>
                </thead>
                <tbody>
                    {logs.map((log, index) => (
                        <tr key={index}>
                            <td>{log[1]}</td>
                            <td>{log[5]}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;
