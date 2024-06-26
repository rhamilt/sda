import { useState } from "react"

import TopKSelector from './TopKSelector'
import StreakSelector from './StreakSelector'
import SkipSelector from './SkipSelector'

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
          <option value="Streak">Streak</option>
          <option value="Skip">Skip</option>
        </select>
      </div>
      <hr/>
      {analysisType === "TopK" && <TopKSelector
                                    onSelect={onSelect}
                                    user={user}
                                    limit={limit} />}

      {analysisType === "Streak" && <StreakSelector
                                    onSelect={onSelect}
                                    user={user}
                                    limit={limit} />}

      {analysisType === "Skip" && <SkipSelector
                                    onSelect={onSelect}
                                    user={user}
                                    limit={limit} />}
    </>
  )
}

export default ModeSelector
