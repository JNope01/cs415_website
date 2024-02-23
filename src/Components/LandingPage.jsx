import React from 'react'
import { useNavigate } from "react-router-dom"

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div>
      <h1>CS415 Landing Page</h1>
      <p><font color="white">This is the publicly accessible page for all users to see</font></p>
    </div>
  )
}

export default LandingPage
