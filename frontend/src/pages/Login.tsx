export default function LoginPage() {
  const handleLogin = () => {
    window.location.href = "http://yourbackend.com/oauth1/start";
  };

  return (
    <div>
      <button onClick={handleLogin}>Login with Yahoo</button>
    </div>
  );
}