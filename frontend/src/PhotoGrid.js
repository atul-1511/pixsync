import React from 'react';
import './App.css';

export default function PhotoGrid({ photos }) {
    return (
        <div className="grid">
            {photos.map(photo => (
                <div key={photo.id} className="photo-item">
                    <img src={photo.url} alt={photo.title} />
                    <div className="caption">{photo.title}</div>
                </div>
            ))}
        </div>
    );
}
