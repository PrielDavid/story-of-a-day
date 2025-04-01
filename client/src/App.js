import React, { useEffect, useState } from 'react';

function App() {
  const [serverMessage, setServerMessage] = useState('');

  useEffect(() => {
    fetch('/api/data')
      .then(response => response.json())
      .then(data => {
        setServerMessage(data.message);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Story of a Day</h1>
      <p>Server says: {serverMessage}</p>
    </div>
  );
}

export default App;
