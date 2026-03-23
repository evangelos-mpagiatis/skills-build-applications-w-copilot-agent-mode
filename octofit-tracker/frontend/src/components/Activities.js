import React, { useState, useEffect } from 'react';

import API_BASE_URL from '../config';
const API_URL = `${API_BASE_URL}/api/activities/`;

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    console.log('Fetching activities from:', API_URL);
    fetch(API_URL)
      .then(response => response.json())
      .then(data => {
        console.log('Activities data:', data);
        const items = data.results || data;
        setActivities(Array.isArray(items) ? items : []);
      })
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div>
      <h2>Activities</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>User</th>
            <th>Activity Type</th>
            <th>Duration (min)</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((activity, index) => (
            <tr key={activity._id || activity.id || index}>
              <td>{activity.user}</td>
              <td>{activity.activity_type}</td>
              <td>{activity.duration}</td>
              <td>{activity.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
