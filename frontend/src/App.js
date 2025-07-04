import React, { useState } from 'react';

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
            setPhotos(data.photos || []);
            setShowImages(true);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Hello from Pixsync frontend!</h1>
            {!showImages && (
                <button onClick={handleShowImages} disabled={loading}>
                    {loading ? 'Loading...' : 'Show Images'}
                </button>
            )}
            {error && <div style={{ color: 'red' }}>{error}</div>}
            {showImages && (
                <>
                    <h2>Photos</h2>
                    <ul>
                        {photos.map(photo => (
                            <li key={photo.id}>
                                <img src={`http://localhost:3030${photo.url}`} alt={photo.title} width={100} />
                                <div>{photo.title}</div>
                            </li>
                        ))}
                    </ul>
                </>
            )}
        </div>
    );
}

export default App;
