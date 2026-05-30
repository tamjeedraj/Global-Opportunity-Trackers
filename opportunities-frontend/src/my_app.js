import React, { useEffect, useState } from "react";

function App() {
  const [opportunities, setOpportunities] = useState([]);
  const [search, setSearch] = useState("");

  // /list से data fetch
  useEffect(() => {
    fetch("http://127.0.0.1:8000/list")
      .then(res => res.json())
      .then(data => setOpportunities(data));
  }, []);

  // /search call
  const handleSearch = () => {
    fetch(`http://127.0.0.1:8000/search?keyword=${search}`)
      .then(res => res.json())
      .then(data => setOpportunities(data));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Opportunities</h1>

      <input
        type="text"
        placeholder="Search by keyword..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>

      <table border="1" style={{ marginTop: "20px", width: "100%" }}>
        <thead>
          <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Category</th>
          </tr>
        </thead>
        <tbody>
          {opportunities.map((opp) => (
            <tr key={opp.id}>
              <td>{opp.title}</td>
              <td>{opp.description}</td>
              <td>{opp.category}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
