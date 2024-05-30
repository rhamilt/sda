import './App.css'
import { useState } from "react"

import ModeSelector from './ModeSelector'
import Display from './Display'

function App() {
  const [data, setData] = useState([])
  const [limit, setLimit] = useState(false)
  const [user, setUser] = useState("")

  return (
    <>
      <p>Spotify Data Analyzer</p>
      <div>
        <label htmlFor="user">Username? </label>
        <input
          type="text"
          id="userInput"
          value={user}
          onChange={(e) => setUser(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="limit">Limit to the current year only? </label>
        <input
          type="checkbox"
          id="limitCheckbox"
          checked={limit}
          onChange={() => setLimit(!limit)}
        />
      </div>
      <ModeSelector limit={limit} user={user} onSelect={setData} />
      {data.length > 0 && <Display data={data}/>}
    </>
  )
}

export default App
