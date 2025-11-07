import React, {useEffect,useState} from 'react';
import API from '../api';

function Dashboard(){
  const [requests,setRequests] = useState([]);
  useEffect(()=> {
    (async ()=>{
      try{
        const token = localStorage.getItem('access');
        if(token) API.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const res = await API.get('services/requests/');
        setRequests(res.data);
      }catch(err){ console.error(err); }
    })();
  },[]);
  return (
    <div style={{padding:20}}>
      <h3>Requests</h3>
      {requests.map(r => (
        <div key={r.id} style={{border:'1px solid #ccc',padding:10,margin:8}}>
          <b>#{r.id}</b> — {r.description}<br/>
          Status: {r.status} — Created: {new Date(r.created_at).toLocaleString()}
        </div>
      ))}
    </div>
  )
}

export default Dashboard;
