import { useRecoilState } from 'recoil';
import { isLoggedInState } from '../states/authState';

function Header() {
  const [isLoggedIn, setIsLoggedIn] = useRecoilState(isLoggedInState);

  const logout = () => {
    setIsLoggedIn(false);
    window.location.href = '/';
  };

  return (
    <header style={{ display: 'flex', justifyContent: 'space-between' }}>
      <h1>Fantasy Data Tools</h1>
      {isLoggedIn && <button onClick={logout}>Logout</button>}
    </header>
  );
}

export default Header;
