import React, { useState, useEffect } from "react";
import { formatTime } from "../utils/formatTime";

function StopWatch() {
  const [seconds, setSeconds] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    let interval;
    if (isRunning) {
      interval = setInterval(() => {
        setSeconds((prev) => prev + 1);
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isRunning]);

  const handleStart = () => setIsRunning(true);
  const handleStop = () => setIsRunning(false);
  const handleReset = () => {
    setIsRunning(false);
    setSeconds(0);
  };

  return (
    <div className="stopwatch-container">
      <h2 className="stopwatch-title">ストップウォッチ</h2>
      <div className="stopwatch-time">{formatTime(seconds)}</div>

      <div className="stopwatch-buttons">
        <button onClick={handleStart} className="btn start">
          スタート
        </button>
        <button onClick={handleStop} className="btn stop">
          ストップ
        </button>
        <button onClick={handleReset} className="btn reset">
          リセット
        </button>
      </div>
    </div>
  );
}

export default StopWatch;
