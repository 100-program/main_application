import React from "react";

function MyPage() {
  // 仮の履歴データ（後でJotaiに置き換え可能）
  const studyHistory = [
    { task: "読書", duration: 1250 }, // 秒数
    { task: "英単語暗記", duration: 600 },
    { task: "数学演習", duration: 1800 },
  ];

  // 秒数を "HH:MM:SS" に変換（formatTimeが使えるならimportしてもOK）
  const formatTime = (totalSeconds) => {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    return `${hours.toString().padStart(2, "0")}:${minutes
      .toString()
      .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
  };

  return (
    <div className="mypage-container">
      <header className="mypage-header">
        <h2 className="mypage-title">勉強履歴</h2>
        <p className="mypage-subtitle">
          StopWatchで記録した学習時間を表示します
        </p>
      </header>

      <main className="mypage-main">
        <section className="history-section">
          <h3>完了したタスク一覧</h3>
          <ul className="history-list">
            {studyHistory.map((entry, index) => (
              <li key={index}>
                ✅ {entry.task}（{formatTime(entry.duration)}）
              </li>
            ))}
          </ul>
        </section>
      </main>
    </div>
  );
}

export default MyPage;
