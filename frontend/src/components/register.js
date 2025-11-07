import React, {useState} from 'react';
import API from '../api';

function Register(){
  const [form,setForm] = useState({username:'',email:'',password:'',is_mechanic:false,phone:''});
  const handle = (e) => setForm({...form, [e.target.name]: e.target.type === 'checkbox' ? e.target.checked : e.target.value});
  const submit = async (e) => {
    e.preventDefault();
    try{
      await API.post('auth/register/', form);
      alert('Registered. Now login.');
    }catch(err){ alert('Error'); }
  }
  return (
    <div style={{padding:20}}>
      <h3>Register</h3>
      <form onSubmit={submit}>
        <input name="username" placeholder="username" value={form.username} onChange={handle}/><br/>
        <input name="email" placeholder="email" value={form.email} onChange={handle}/><br/>
        <input name="password" placeholder="password" type="password" value={form.password} onChange={handle}/><br/>
        <input name="phone" placeholder="phone" value={form.phone} onChange={handle}/><br/>
        <label><input type="checkbox" name="is_mechanic" checked={form.is_mechanic} onChange={handle}/> Register as mechanic</label><br/>
        <button>Register</button>
      </form>
    </div>
  )
}

export default Register;
