import React, { useState, useEffect } from 'react';
import BASE_URL from '../config';

import API_BASE_URL from '../config';
const API_URL = `${API_BASE_URL}/api/workouts/`;

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    console.log('Fetching workouts from:', API_URL);
    fetch(API_URL)
      .then(response => response.json())
      .then(data => {
        console.log('Workouts data:', data);
        const items = data.results || data;
        setWorkouts(Array.isArray(items) ? items : []);
      })
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div>
      <h2>Workouts</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout, index) => (
            <tr key={workout._id || workout.id || index}>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;
