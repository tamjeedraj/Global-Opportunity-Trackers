// "use client";

// import { useState } from "react";

// const opportunities = [
//   {
//     id: 1,
//     title: "Google for Startups Accelerator",
//     country: "Singapore",
//     category: "Startup",
//     deadline: "2026-06-30",
//     funding: "$100,000",
//     status: "Saved",
//   },
//   {
//     id: 2,
//     title: "UNESCO Youth Fellowship",
//     country: "France",
//     category: "Research",
//     deadline: "2026-07-15",
//     funding: "Fully Funded",
//     status: "Applied",
//   },
//   {
//     id: 3,
//     title: "Women Founder Grant",
//     country: "Germany",
//     category: "Women",
//     deadline: "2026-08-10",
//     funding: "$50,000",
//     status: "Planning",
//   },
// ];

// export default function Dashboard() {
//   const [search, setSearch] = useState("");

//   const filtered = opportunities.filter(
//     (item) =>
//       item.title.toLowerCase().includes(search.toLowerCase()) ||
//       item.category.toLowerCase().includes(search.toLowerCase()) ||
//       item.country.toLowerCase().includes(search.toLowerCase())
//   );

//   return (
//     <div className="min-h-screen bg-slate-100 p-6">
//       <h1 className="text-4xl font-bold mb-6">
//         Global Opportunity Tracker
//       </h1>

//       {/* Stats */}
//       <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
//         <div className="bg-white rounded-xl p-5 shadow">
//           <h3 className="text-gray-500">Total Opportunities</h3>
//           <p className="text-3xl font-bold">4250</p>
//         </div>

//         <div className="bg-white rounded-xl p-5 shadow">
//           <h3 className="text-gray-500">Upcoming Deadlines</h3>
//           <p className="text-3xl font-bold">87</p>
//         </div>

//         <div className="bg-white rounded-xl p-5 shadow">
//           <h3 className="text-gray-500">Saved</h3>
//           <p className="text-3xl font-bold">124</p>
//         </div>

//         <div className="bg-white rounded-xl p-5 shadow">
//           <h3 className="text-gray-500">Applied</h3>
//           <p className="text-3xl font-bold">32</p>
//         </div>
//       </div>

//       {/* Search */}
//       <div className="bg-white p-4 rounded-xl shadow mb-8">
//         <input
//           type="text"
//           placeholder="Search opportunities..."
//           className="w-full border p-3 rounded-lg"
//           value={search}
//           onChange={(e) => setSearch(e.target.value)}
//         />
//       </div>

//       {/* Opportunities */}
//       <div className="mb-10">
//         <h2 className="text-2xl font-semibold mb-4">
//           Opportunities
//         </h2>

//         <div className="grid gap-4">
//           {filtered.map((item) => (
//             <div
//               key={item.id}
//               className="bg-white rounded-xl shadow p-5"
//             >
//               <div className="flex justify-between">
//                 <div>
//                   <h3 className="text-xl font-bold">
//                     {item.title}
//                   </h3>

//                   <p className="text-gray-600">
//                     {item.country} • {item.category}
//                   </p>

//                   <p className="mt-2">
//                     Funding: {item.funding}
//                   </p>

//                   <p>
//                     Deadline: {item.deadline}
//                   </p>
//                 </div>

//                 <button className="bg-blue-600 text-white px-4 py-2 rounded-lg h-fit">
//                   Save
//                 </button>
//               </div>
//             </div>
//           ))}
//         </div>
//       </div>

//       {/* Application Tracker */}
//       <div>
//         <h2 className="text-2xl font-semibold mb-4">
//           Application Tracker
//         </h2>

//         <div className="grid md:grid-cols-3 gap-4">
//           <div className="bg-white p-4 rounded-xl shadow">
//             <h3 className="font-bold mb-3">Saved</h3>

//             {opportunities
//               .filter((o) => o.status === "Saved")
//               .map((o) => (
//                 <div
//                   key={o.id}
//                   className="bg-slate-100 p-3 rounded mb-2"
//                 >
//                   {o.title}
//                 </div>
//               ))}
//           </div>

//           <div className="bg-white p-4 rounded-xl shadow">
//             <h3 className="font-bold mb-3">
//               Planning
//             </h3>

//             {opportunities
//               .filter((o) => o.status === "Planning")
//               .map((o) => (
//                 <div
//                   key={o.id}
//                   className="bg-slate-100 p-3 rounded mb-2"
//                 >
//                   {o.title}
//                 </div>
//               ))}
//           </div>

//           <div className="bg-white p-4 rounded-xl shadow">
//             <h3 className="font-bold mb-3">
//               Applied
//             </h3>

//             {opportunities
//               .filter((o) => o.status === "Applied")
//               .map((o) => (
//                 <div
//                   key={o.id}
//                   className="bg-slate-100 p-3 rounded mb-2"
//                 >
//                   {o.title}
//                 </div>
//               ))}
//           </div>
//         </div>
//       </div>

//       {/* AI Search Assistant */}
//       <div className="mt-10 bg-white rounded-xl p-6 shadow">
//         <h2 className="text-2xl font-semibold mb-4">
//           AI Search Assistant
//         </h2>

//         <div className="border rounded-lg p-4 bg-slate-50">
//           <p className="font-medium">
//             User:
//           </p>
//           <p>
//             Women founder grants in Europe
//           </p>

//           <div className="mt-4">
//             <p className="font-medium text-green-700">
//               AI:
//             </p>

//             <p>
//               Found 18 matching opportunities across
//               Germany, France, Netherlands and Sweden.
//             </p>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// }

// "use client";

// import { useState } from "react";

// const opportunities = [
//   {
//     id: 1,
//     title: "Google Startup Accelerator",
//     country: "Singapore",
//     deadline: "30 Jun 2026",
//     status: "Applied",
//   },
//   {
//     id: 2,
//     title: "Women Founder Grant",
//     country: "Germany",
//     deadline: "12 Jul 2026",
//     status: "Saved",
//   },
//   {
//     id: 3,
//     title: "MIT Research Fellowship",
//     country: "USA",
//     deadline: "18 Aug 2026",
//     status: "Planning",
//   },
// ];

// export default function Dashboard() {
//   const [search, setSearch] = useState("");
//   const [country, setCountry] = useState("All");

//   const filtered = opportunities.filter((item) => {
//     const matchSearch = item.title
//       .toLowerCase()
//       .includes(search.toLowerCase());

//     const matchCountry =
//       country === "All" || item.country === country;

//     return matchSearch && matchCountry;
//   });

//   return (
//     <div className="min-h-screen bg-slate-100">
//       {/* Header */}
//       <header className="bg-white shadow p-5">
//         <h1 className="text-3xl font-bold">
//           Global Opportunity Tracker
//         </h1>
//       </header>

//       <div className="p-6 grid lg:grid-cols-4 gap-6">

//         {/* Left Sidebar */}
//         <div className="bg-white rounded-xl p-5 shadow">
//           <h2 className="font-bold mb-4">Filters</h2>

//           <select
//             className="w-full border p-2 rounded"
//             value={country}
//             onChange={(e) => setCountry(e.target.value)}
//           >
//             <option>All</option>
//             <option>USA</option>
//             <option>Germany</option>
//             <option>Singapore</option>
//           </select>

//           <div className="mt-6">
//             <h3 className="font-semibold mb-2">
//               Saved Opportunities
//             </h3>

//             <ul className="space-y-2">
//               {opportunities
//                 .filter((x) => x.status === "Saved")
//                 .map((x) => (
//                   <li
//                     key={x.id}
//                     className="bg-slate-100 p-2 rounded"
//                   >
//                     {x.title}
//                   </li>
//                 ))}
//             </ul>
//           </div>
//         </div>

//         {/* Center Section */}
//         <div className="lg:col-span-2 space-y-5">

//           {/* Search */}
//           <div className="bg-white p-4 rounded-xl shadow">
//             <input
//               placeholder="Search opportunities..."
//               className="w-full border p-3 rounded-lg"
//               value={search}
//               onChange={(e) => setSearch(e.target.value)}
//             />
//           </div>

//           {/* Opportunity List */}
//           <div className="bg-white p-5 rounded-xl shadow">
//             <h2 className="text-xl font-bold mb-4">
//               Opportunities
//             </h2>

//             <div className="space-y-3">
//               {filtered.map((item) => (
//                 <div
//                   key={item.id}
//                   className="border rounded-lg p-4"
//                 >
//                   <h3 className="font-bold">
//                     {item.title}
//                   </h3>

//                   <p className="text-sm text-gray-500">
//                     {item.country}
//                   </p>

//                   <p className="text-sm">
//                     Deadline: {item.deadline}
//                   </p>

//                   <span className="inline-block mt-2 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">
//                     {item.status}
//                   </span>
//                 </div>
//               ))}
//             </div>
//           </div>

//           {/* AI Recommendations */}
//           <div className="bg-white p-5 rounded-xl shadow">
//             <h2 className="text-xl font-bold mb-4">
//               AI Recommendations
//             </h2>

//             <div className="space-y-2">
//               <div className="bg-green-50 p-3 rounded">
//                 UNESCO Youth Fellowship
//               </div>

//               <div className="bg-green-50 p-3 rounded">
//                 Google AI Startup Program
//               </div>

//               <div className="bg-green-50 p-3 rounded">
//                 Women Techmakers Scholarship
//               </div>
//             </div>
//           </div>
//         </div>

//         {/* Right Sidebar */}
//         <div className="space-y-5">

//           {/* Deadline Calendar */}
//           <div className="bg-white p-5 rounded-xl shadow">
//             <h2 className="font-bold mb-4">
//               Deadline Calendar
//             </h2>

//             <ul className="space-y-3">
//               <li>
//                 📅 30 Jun - Google Startup Accelerator
//               </li>

//               <li>
//                 📅 12 Jul - Women Founder Grant
//               </li>

//               <li>
//                 📅 18 Aug - MIT Fellowship
//               </li>
//             </ul>
//           </div>

//           {/* Status Tracker */}
//           <div className="bg-white p-5 rounded-xl shadow">
//             <h2 className="font-bold mb-4">
//               Status Tracker
//             </h2>

//             <div className="space-y-2">
//               <div className="flex justify-between">
//                 <span>Saved</span>
//                 <span>5</span>
//               </div>

//               <div className="flex justify-between">
//                 <span>Planning</span>
//                 <span>8</span>
//               </div>

//               <div className="flex justify-between">
//                 <span>Applied</span>
//                 <span>12</span>
//               </div>

//               <div className="flex justify-between">
//                 <span>Interview</span>
//                 <span>2</span>
//               </div>

//               <div className="flex justify-between">
//                 <span>Accepted</span>
//                 <span>1</span>
//               </div>
//             </div>
//           </div>
//         </div>

//       </div>
//     </div>
//   );
// }

"use client";

import { useState, useEffect } from "react";
import axios from "axios";

export default function Dashboard() {
  const [search, setSearch] = useState("");
  const [country, setCountry] = useState("All");
  const [opportunities, setOpportunities] = useState([]);
  const [recommendations, setRecommendations] = useState([]);

  // 🔹 Fetch opportunities & recommendations automatically
  useEffect(() => {
    const fetchData = async () => {
      try {
        const oppRes = await axios.get("http://localhost:8000/api/opportunities");
        setOpportunities(oppRes.data);

        const recRes = await axios.get("http://localhost:8000/api/recommendations");
        setRecommendations(recRes.data);
      } catch (err) {
        console.error("Error fetching data:", err);
      }
    };

    fetchData();

    // 🔹 Auto-refresh every 6 hours
    const interval = setInterval(fetchData, 21600000);
    return () => clearInterval(interval);
  }, []);

  // 🔹 Deadline alert automation
  useEffect(() => {
    const today = new Date();
    opportunities.forEach((opp) => {
      const diff = (new Date(opp.deadline) - today) / (1000 * 60 * 60 * 24);
      if (diff <= 3 && diff > 0) {
        console.log(`⚠️ Deadline approaching for ${opp.title}`);
      }
    });
  }, [opportunities]);

  // 🔹 Filter logic
  const filtered = opportunities.filter((item) => {
    const matchSearch = item.title.toLowerCase().includes(search.toLowerCase());
    const matchCountry = country === "All" || item.country === country;
    return matchSearch && matchCountry;
  });

  return (
    <div className="min-h-screen bg-slate-100">
      {/* Header */}
      <header className="bg-white shadow p-5">
        <h1 className="text-3xl font-bold">Global Opportunity Tracker</h1>
      </header>

      <div className="p-6 grid lg:grid-cols-4 gap-6">
        {/* Left Sidebar */}
        <div className="bg-white rounded-xl p-5 shadow">
          <h2 className="font-bold mb-4">Filters</h2>

          <select
            className="w-full border p-2 rounded"
            value={country}
            onChange={(e) => setCountry(e.target.value)}
          >
            <option>All</option>
            <option>USA</option>
            <option>Germany</option>
            <option>Singapore</option>
          </select>

          <div className="mt-6">
            <h3 className="font-semibold mb-2">Saved Opportunities</h3>
            <ul className="space-y-2">
              {opportunities
                .filter((x) => x.status === "Saved")
                .map((x) => (
                  <li key={x.id} className="bg-slate-100 p-2 rounded">
                    {x.title}
                  </li>
                ))}
            </ul>
          </div>
        </div>

        {/* Center Section */}
        <div className="lg:col-span-2 space-y-5">
          {/* Search */}
          <div className="bg-white p-4 rounded-xl shadow">
            <input
              placeholder="Search opportunities..."
              className="w-full border p-3 rounded-lg"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </div>

          {/* Opportunity List */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h2 className="text-xl font-bold mb-4">Opportunities</h2>
            <div className="space-y-3">
              {filtered.map((item) => (
                <div key={item.id} className="border rounded-lg p-4">
                  <h3 className="font-bold">{item.title}</h3>
                  <p className="text-sm text-gray-500">{item.country}</p>
                  <p className="text-sm">Deadline: {item.deadline}</p>
                  <span className="inline-block mt-2 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">
                    {item.status}
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* AI Recommendations */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h2 className="text-xl font-bold mb-4">AI Recommendations</h2>
            <div className="space-y-2">
              {recommendations.map((rec, i) => (
                <div key={i} className="bg-green-50 p-3 rounded">
                  {rec.title}
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Right Sidebar */}
        <div className="space-y-5">
          {/* Deadline Calendar */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h2 className="font-bold mb-4">Deadline Calendar</h2>
            <ul className="space-y-3">
              {opportunities.map((x) => (
                <li key={x.id}>📅 {x.deadline} - {x.title}</li>
              ))}
            </ul>
          </div>

          {/* Status Tracker */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h2 className="font-bold mb-4">Status Tracker</h2>
            <div className="space-y-2">
              {["Saved", "Planning", "Applied", "Interview", "Accepted"].map((status) => (
                <div key={status} className="flex justify-between">
                  <span>{status}</span>
                  <span>{opportunities.filter((x) => x.status === status).length}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
