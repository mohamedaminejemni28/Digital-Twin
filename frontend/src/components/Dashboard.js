import React, { useEffect, useState } from 'react';
import Charts from './Charts';

function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/data');
    ws.onmessage = (event) => {
      const parsedData = JSON.parse(event.data);
      setData((prev) => [...prev.slice(-50), parsedData]);
    };
    return () => ws.close();
  }, []);

  return (
    <div>
      <Charts data={data} />
    </div>
  );
}

export default Dashboard;
