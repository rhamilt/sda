const Display = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Time (min)</th>
        </tr>
      </thead>
      <tbody>
        {data.map((pair) => (
          <tr key={pair.key}>
            <td>{pair.key}</td>
            <td>{pair.total}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}

export default Display
