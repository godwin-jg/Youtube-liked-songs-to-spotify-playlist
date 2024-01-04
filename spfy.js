// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token =
  "BQDf7qUXoNuW6g9wnXqpAvShhcDbQuDCOvbKxJgNXypxzAPC6xhBMEES0bE9enH1rKcNybnWS_EZkE-9ouns5ouaFrlqWNPFlBrHBb4Af8pWufsuoIRzbA-HNDUXUcCA5k5M12RvbLFLhhjKzx7S4UM3ry3KFI6Y-mfjg8N-5KW7uLngsjRtKMnS2LE0cX6jHnrnrOwMeTOVo2Sl6QXUJO5YKWFYkMpGQ6CuXHGM86cW7XG8VG7zqAA9XGiBRXhzb1Y6BjDZ8k73zsq8K7Y2nRGmzTmP";
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body: JSON.stringify(body),
  });
  return await res.json();
}

async function getTopTracks() {
  // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (
    await fetchWebApi("v1/me/top/tracks?time_range=long_term&limit=5", "GET")
  ).items;
}

const topTracks = await getTopTracks();
console.log(
  topTracks?.map(
    ({ name, artists }) =>
      `${name} by ${artists.map((artist) => artist.name).join(", ")}`
  )
);
