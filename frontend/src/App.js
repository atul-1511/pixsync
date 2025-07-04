import React, { useState } from 'react';
import PhotoGrid from './PhotoGrid';
import './App.css';

function App() {
    const [photos, setPhotos] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleShowPhotos = async () => {
        setLoading(true);
        setError(null);
        try {
            const res = await fetch('http://localhost:9000/photos');
            if (!res.ok) throw new Error(res.statusText);
            const data = await res.json();
            setPhotos(data.photos);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    if (loading) {
        return <div className="button-center">Loading…</div>;
    }
    if (error) {
        return <div className="button-center">Error: {error}</div>;
    }

    return (
        <div>
            {photos.length === 0 ? (
                <div className="button-center">
                    <button onClick={handleShowPhotos}>Show Photos</button>
                </div>
            ) : (
                <PhotoGrid photos={photos} />
            )}
        </div>
    );
}

export default App;
