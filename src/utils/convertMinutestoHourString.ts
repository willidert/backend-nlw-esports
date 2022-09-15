export function convertMinutesToHourString(minutesAmount: number) {
  const hour = Math.floor(minutesAmount / 60);

  const minutes = minutesAmount % 60;

  const minutesString = minutes < 10 ? `0${minutes}` : minutes;

  return [hour, minutesString].join(":");
}
