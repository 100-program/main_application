import React, { useState } from "react";

function Shop() {
  const [gems, setGems] = useState(100);
  const [ownedAvatars, setOwnedAvatars] = useState([]);
  const [selectedAvatar, setSelectedAvatar] = useState(null);

  const avatars = [
    { id: 1, name: "アバター1", cost: 30 },
    { id: 2, name: "アバター2", cost: 50 },
    { id: 3, name: "アバター3", cost: 20 },
  ];

  const handlePurchase = (avatar) => {
    if (gems >= avatar.cost && !ownedAvatars.includes(avatar.id)) {
      setGems((prev) => prev - avatar.cost);
      setOwnedAvatars((prev) => [...prev, avatar.id]);
    }
  };

  const handleSelect = (avatarId) => {
    if (ownedAvatars.includes(avatarId)) {
      setSelectedAvatar(avatarId);
    }
  };

  return (
    <div className="shop-container">
      <header className="shop-header">
        <h2 className="shop-title">アバターショップ</h2>
        <div className="gem-display">
          💎 <span>{gems}</span>
        </div>
      </header>

      <main className="shop-main">
        <ul className="avatar-list">
          {avatars.map((avatar) => (
            <li key={avatar.id} className="avatar-card">
              <span>{avatar.name}</span>
              <span>{avatar.cost}💎</span>
              <button
                onClick={() => handlePurchase(avatar)}
                disabled={
                  gems < avatar.cost || ownedAvatars.includes(avatar.id)
                }
              >
                {ownedAvatars.includes(avatar.id) ? "購入済み" : "購入"}
              </button>
              {ownedAvatars.includes(avatar.id) && (
                <button
                  onClick={() => handleSelect(avatar.id)}
                  disabled={selectedAvatar === avatar.id}
                >
                  {selectedAvatar === avatar.id ? "選択中" : "選択"}
                </button>
              )}
            </li>
          ))}
        </ul>

        {selectedAvatar && (
          <div className="selected-preview">
            <p>現在のアバター: アバター{selectedAvatar}</p>
            {/* TODO: Avatar.jsx に連動して表示切り替え */}
          </div>
        )}
      </main>
    </div>
  );
}

export default Shop;
