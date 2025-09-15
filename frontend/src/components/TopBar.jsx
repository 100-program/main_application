import React from "react";
import { Link } from "react-router-dom";
import "./TopBar.css";

function TopBar({ gemCount = 0 }) {
  return (
    <header className="topbar">
      <div className="topbar-left">
        <span className="app-name">Norsona</span>
      </div>

      <div className="topbar-center">
        <div className="gem-display">
          💎 <span>{gemCount}</span>
        </div>
      </div>

      <div className="topbar-right">
        <Link to="/mypage" className="topbar-button">
          CUSTOMIZE
        </Link>
        <Link to="/shop" className="topbar-button">
          SHOP
        </Link>
      </div>
    </header>
  );
}

export default TopBar;
