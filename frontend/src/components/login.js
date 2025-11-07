import React, {useState} from 'react';
import API, {setAuthToken} from '../api';

function Login(){
  const [username,setUsername] = useState('');
  const [password,setPassword] = useState('');
  const onSubmit = async (e) => {
    e.preventDefault();
    try{
      const res = await API.post('token/', {username, password});
      localStorage.setItem('access', res.data.access);
      setAuthToken(res.data.access);
      alert('Logged in');
    }catch(err){
      alert('Error logging in');
    }
  }
  return (
    <div style={{padding:20}}>
      <h3>Login</h3>
      <form onSubmit={onSubmit}>
        <input placeholder="username" value={username} onChange={e=>setUsername(e.target.value)} /><br/>
        <input placeholder="password" value={password} type="password" onChange={e=>setPassword(e.target.value)} /><br/>
        <button>Login</button>
      </form>
    </div>
  )
}

export default Login;
