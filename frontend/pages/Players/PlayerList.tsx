import Image from 'next/image';

export default function PlayerList(playerData) {
  const { name, position, team, stats, image } = playerData.playerName;

  return (
    <div>
      <Image src={image} alt={name} width="100" height="100" layout="responsive"/>
    </div>
  );
}