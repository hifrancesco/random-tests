import React, { useState, useEffect } from "react";

const App = () => {
    const [repos, setRepos] = useState([]);

    useEffect(() => {
    const fetchData = async () => {
        const res = await fetch("https://api.github.com/users/{francescowang}/repos");
        const data = await res.json();
        setRepos(data);
    };
    fetchData();
}, []);

    return (
    <div>
        <h1>GitHub Repositories</h1>
        {repos.map(repo => (
        <div key={repo.id}>
            <h2>{repo.name}</h2>
            <p>{repo.description}</p>
        </div>
    ))}
    </div>
    );
};

export default App;
