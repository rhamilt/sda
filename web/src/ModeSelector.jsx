import { useState } from "react"

import TopKSelector from './TopKSelector'

const ModeSelector = ({ user, limit, onSelect }) => {
  const [analysisType, setAnalysisType] = useState("TopK")
  return (
    <>
      <div>
        <label htmlFor="analysisType">Analysis Type:</label>
        <select
          id="analysisType"
          onChange={(e) => setAnalysisType(e.target.value)}>
          <option value="TopK">Top K</option>
        </select>
      </div>
      <hr/>
      {analysisType === "TopK" && <TopKSelector
                                    onSelect={onSelect}
                                    user={user}
                                    limit={limit} />}
    </>
  )
}

export default ModeSelector
