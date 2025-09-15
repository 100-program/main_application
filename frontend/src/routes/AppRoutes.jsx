import React from "react";
import { Routes, Route } from "react-router-dom";
import Dashboard from "../pages/Dashboard";
import MyPage from "../pages/MyPage";
import Shop from "../pages/Shop";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/mypage" element={<MyPage />} />
      <Route path="/shop" element={<Shop />} />
    </Routes>
  );
}

export default AppRoutes;
