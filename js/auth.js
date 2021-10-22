import fetch from 'node-fetch';

const host = 'https://wallet.testnet.vega.xyz/api/v1';

main().then(() => {}, err => {
  console.log(err);
  process.exit(-1);
})

async function main () {
  const [a, b, wallet, passphrase] = process.argv;

  const {token} = await request({
    endpoint:'/auth/token',
    method: 'POST',
    body: {
      wallet,
      passphrase,
    },
  });
  console.log({token});

  const {keys} = await request({
    endpoint:'/keys',
    method: 'GET',
    token
  });
  console.log({keys: keys.map(k => k.pub)});
}

async function request({
  token,
  endpoint,
  method,
  body,
}) {
  const opts = {
    method,
    headers: {
      'content-type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
  };
  if (body) {
    opts.body = JSON.stringify(body);
  }

  const res = await fetch(host + endpoint, opts);
  return await res.json();
}