import OAuth from "../components/OAuth";
import { Button, Card, Checkbox, Label, TextInput } from "flowbite-react";
import { useState } from "react";
import { useDispatch } from 'react-redux';
import { signInSuccess } from '../redux/user/userSlice';
import { useNavigate } from 'react-router-dom';

export default function Login(){

    const BASE_API=import.meta.env.VITE_API_BASE_URL;
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const [formData, setFormData]= useState({username:'', password:''});
    const handleChange=(e)=>{
      setFormData({...formData, [e.target.name]:e.target.value})
    }

    const handleClick= async(e) =>{
      e.preventDefault();
      const res= await fetch(`${BASE_API}/api/auth/login`,{
        method:"POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      })

      if(res.ok){
        const data= await res.json();
        // console.log(data.access)
        const userRes= await fetch(`${BASE_API}/api/auth/getUser`,{
          method:"POST",
          headers:{
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${data.access}`
          },
          body: JSON.stringify(formData),
        }) 
        const userData= await userRes.json();
        userData['accessToken']=data.access;
        console.log(userData);      
        dispatch(signInSuccess(userData))  
        navigate('/')
      }

    }

    return (
        <div className="min-h-screen flex justify-center items-center bg-gray-900">

          <Card className="max-w-sm">
            <form className="flex flex-col gap-4" onSubmit={handleClick}>
              <div>
                <div className="mb-2 block">
                  <Label htmlFor="username" value="Username" />
                </div>
                <TextInput onChange={handleChange} id="username" type="text" name="username" placeholder="username" required />
              </div>
              <div>
                <div className="mb-2 block">
                  <Label htmlFor="password1" value="password" />
                </div>
                <TextInput onChange={handleChange} id="password1" type="password" name="password" required />
              </div>
              <Button type="submit">Submit</Button>
            </form>
          </Card>          
          
          {/* <OAuth/> */}
        </div>        
      );    
}