import React, { useState } from 'react';
import './App.css';

function App() {
    const [photos, setPhotos] = useState([]);
    const [showImages, setShowImages] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleShowImages = async () => {
        setLoading(true);
        setError(null);
        try {
            const res = await fetch('http://localhost:3030/v1/photos/');
            if (!res.ok) throw new Error(res.statusText);
            const data = await res.json();
            console.log('Photos data:', data);
            console.log('Number of photos:', data.photos?.length || 0);
            setPhotos(data.photos || []);
            setShowImages(true);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    // Calculate grid columns based on number of photos
    const getGridColumns = (photoCount) => {
        console.log('Calculating grid columns for', photoCount, 'photos');
        if (photoCount <= 4) return photoCount;
        if (photoCount <= 9) return 3;
        if (photoCount <= 16) return 4;
        if (photoCount <= 25) return 5;
        return 6; // Max 6 columns for larger sets
    };

    const gridColumns = getGridColumns(photos.length);
    const gridClassName = `photo-grid photo-grid-${gridColumns}`;

    console.log('Grid columns:', gridColumns);
    console.log('Grid class name:', gridClassName);

    return (
        <div className="app">
            <h1>Hello from Pixsync frontend!</h1>
            {!showImages && (
                <button onClick={handleShowImages} disabled={loading}>
                    {loading ? 'Loading...' : 'Show Images'}
                </button>
            )}
            {error && <div style={{ color: 'red' }}>{error}</div>}
            {showImages && (
                <>
                    <h2>Photos ({photos.length} images) - Grid: {gridColumns} columns</h2>
                    <div style={{ marginBottom: '20px', padding: '10px', backgroundColor: '#f0f0f0', borderRadius: '5px' }}>
                        <strong>Debug Info:</strong><br />
                        Photos count: {photos.length}<br />
                        Grid columns: {gridColumns}<br />
                        CSS class: {gridClassName}
                    </div>
                    <div className={gridClassName}>
                        {photos.map(photo => (
                            <div key={photo.id} className="photo-card">
                                <img
                                    src={`http://localhost:3030${photo.url}`}
                                    alt={photo.title}
                                    className="photo-image"
                                />
                                <div className="photo-title">{photo.title}</div>
                            </div>
                        ))}
                    </div>
                </>
            )}
        </div>
    );
}

export default App;
