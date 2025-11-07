import React, {useState, useEffect} from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import API, { setAuthToken } from '../api';

function MapRequest(){
  const [position,setPosition] = useState([28.6139,77.2090]);
  const [description,setDescription] = useState('');
  const [nearby,setNearby] = useState([]);
  useEffect(()=>{
    const token = localStorage.getItem('access');
    setAuthToken(token);
    if(navigator.geolocation){
      navigator.geolocation.getCurrentPosition(p=>{
        setPosition([p.coords.latitude, p.coords.longitude]);
      });
    }
  },[]);
  const findNearby = async ()=> {
    const res = await API.get(`services/requests/nearby_mechanics/?lat=${position[0]}&lon=${position[1]}&radius=10`);
    setNearby(res.data);
  };
  const createRequest = async ()=> {
    const payload = {description, latitude: position[0], longitude: position[1]};
    try{
      const res = await API.post('services/requests/', payload);
      alert('Request created: ' + res.data.id);
    }catch(err){ alert('Create failed'); }
  }

  return (
    <div style={{display:'flex',gap:20,padding:20}}>
      <div style={{width:'70%'}}>
        <MapContainer center={position} zoom={13} style={{height:500}}>
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
          <Marker position={position}>
            <Popup>Your location</Popup>
          </Marker>
          {nearby.map((m,idx)=>(
            <Marker key={idx} position={[m.latitude, m.longitude]}>
              <Popup>{m.username} — {m.skills} — {m.distance_km} km</Popup>
            </Marker>
          ))}
        </MapContainer>
      </div>
      <div style={{width:'30%'}}>
        <h3>Request Service</h3>
        <textarea placeholder="Describe issue" value={description} onChange={e=>setDescription(e.target.value)} style={{width:'100%',height:120}}/>
        <button onClick={createRequest}>Send Request</button>
        <hr/>
        <button onClick={findNearby}>Find Nearby Mechanics</button>
        <div>
          {nearby.map((m)=>(
            <div key={m.mechanic_id} style={{border:'1px solid #ccc',padding:8,marginTop:8}}>
              <b>{m.username}</b><br/>{m.skills}<br/>Rating: {m.rating} — {m.distance_km} km
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default MapRequest;
