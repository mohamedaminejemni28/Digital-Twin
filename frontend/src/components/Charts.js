import React from 'react';
import { Line } from 'react-chartjs-2';

function Charts({ data }) {
  const timeLabels = data.map(d => new Date(d.timestamp).toLocaleTimeString());
  const heartRate = data.map(d => d.heart_rate);
  const speed = data.map(d => d.speed);

  const chartData = {
    labels: timeLabels,
    datasets: [
      {
        label: 'Heart Rate',
        data: heartRate,
        borderColor: 'red',
        fill: false,
      },
      {
        label: 'Speed',
        data: speed,
        borderColor: 'blue',
        fill: false,
      },
    ],
  };

  return (
    <div>
      <Line data={chartData} />
    </div>
  );
}

export default Charts;
