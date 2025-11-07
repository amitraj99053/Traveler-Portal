import React, {useEffect,useState} from 'react';
import API from '../api';

function MechanicsList(){
  const [list,setList] = useState([]);
  useEffect(()=> {
    (async ()=>{
      // Use a sample center for listing
      const res = await API.get(`services/requests/nearby_mechanics/?lat=28.6139&lon=77.2090&radius=50`);
      setList(res.data);
    })();
  },[]);
  return (
    <div style={{padding:20}}>
      <h3>Mechanics</h3>
      {list.map(m => (
        <div key={m.mechanic_id} style={{border:'1px solid #ddd',padding:10,margin:8}}>
          <b>{m.username}</b> — {m.skills}<br/>Distance: {m.distance_km} km — Rating: {m.rating}
        </div>
      ))}
    </div>
  )
}

export default MechanicsList;
