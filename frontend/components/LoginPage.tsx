import { useEffect } from 'react';
import { useRecoilState } from 'recoil';
import { isLoggedInState } from '../states/authState';
import axios from 'axios';

function LoginPage() {
  const [isLoggedIn, setIsLoggedIn] = useRecoilState(isLoggedInState);

  const initiateLogin = async () => {
    try {
      const response = await axios.get('http://localhost:8000/oauth1_start');
      window.location.href = response.data.authorization_url;
    } catch (error) {
      console.error('Error initiating login:', error);
    }
  };

  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');

    if (code) {
      // exchange the code for an access token and set isLoggedIn to true
      // ...
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <div>
      {!isLoggedIn && <button onClick={initiateLogin}>Login with Yahoo</button>}
    </div>
  );
}

export default LoginPage;
