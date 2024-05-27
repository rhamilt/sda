import { useState } from "react"

const TopKSelector = ({ user, limit, onSelect }) => {
  const [k, setK] = useState("1")
  const [type, setType] = useState("Song")

  const onSubmit = async (e) => {
    e.preventDefault()

    const data = {
      k,
      type,
      limit
    }

    const url=`http://127.0.0.1:5000/${user}/topK`
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data)
    }

    const response = await fetch(url, options)
    const result = await response.json()
    if (response.status !== 201 && response.status !== 200) {
      alert(result.message)
    } else {
      onSelect(result.data)
    }
  }

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="k">K:</label>
        <input
          type="number"
          value={k}
          id="k"
          onChange={(e) => setK(e.target.value)}
          min="1"
          max="250"
        />
      </div>

      <div>
        <label htmlFor="type">Type:</label>
        <select
          id="type"
          value={type}
          onChange={(e) => setType(e.target.value)}>
          <option value="Song">Song</option>
          <option value="Artist">Artist</option>
          <option value="Hour">Hour</option>
          <option value="Month">Month</option>
        </select>
      </div>
    </form>
  )
}

export default TopKSelector
