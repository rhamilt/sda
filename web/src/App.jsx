import './App.css'
import { useState } from "react"

import ModeSelector from './ModeSelector'
import Display from './Display'

function App() {
  const [data, setData] = useState([])

  const limit = true

  return (
    <>
      <p>Spotify Data Analyzer</p>
      <ModeSelector limit user={"rhamilt"} onSelect={setData} />
      {data && <Display data={data}/>}
    </>
  )
}

export default App
