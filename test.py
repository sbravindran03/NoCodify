import execjs

# create a JavaScript context
ctx = execjs.compile("""
    const web3 = require("@solana/web3.js");
(async () => {
  const publicKey = new web3.PublicKey(
    "E645TckHQnDcavVv92Etc6xSWQaq8zzPtPRGBheviRAk"
  );
  const solanaConnection = new web3.Connection("http://sample-endpoint-name.network.quiknode.pro/token-goes-here/", {
    wsEndpoint: "wss://sample-endpoint-name.network.quiknode.pro/token-goes-here/",
  });
  solanaConnection.onAccountChange(
    publicKey,
    (updatedAccountInfo, context) =>
      console.log("Updated account info: ", updatedAccountInfo),
    "confirmed"
  );
})();

""")
print(ctx)

# call a JavaScript function with arguments
# result = ctx.call("add", 2, 3)
# print(result)