using System;
using System.Security.Cryptography;
using System.Text;
using System.IO;

namespace rsa_new
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length < 2)
            {
                Console.WriteLine("Usage:");
                Console.WriteLine("  Encrypt: rsa.exe encrypt <MANV> <LUONGCB> <MK>");
                Console.WriteLine("  Decrypt: rsa.exe decrypt <MANV> <MK> <EncryptedHex>");
                return;
            }

            string mode = args[0].ToLower();

            if (mode == "encrypt" && args.Length == 4)
            {
                EncryptLuong(args[1], args[2], args[3]);
            }
            else if (mode == "decrypt" && args.Length == 4)
            {
                DecryptLuong(args[1], args[2], args[3]);
            }
            else
            {
                Console.WriteLine("Invalid arguments.");
            }
        }

        // 🔐 Hàm mã hóa (Updated to return VARBINARY type)
        static void EncryptLuong(string manv, string luong, string mk)
        {
            using (RSACryptoServiceProvider rsa = new RSACryptoServiceProvider(512))
            {
                // Lưu private key
                string tempDirectory = @"D:\Temp";  // Specify a directory with write access
                if (!Directory.Exists(tempDirectory))
                {
                    Directory.CreateDirectory(tempDirectory);  // Create the directory if it doesn't exist
                }

                string privateKeyXml = rsa.ToXmlString(true);
                string privateKeyPath = Path.Combine(tempDirectory, $"private_{manv}_{mk}.xml");
                File.WriteAllText(privateKeyPath, privateKeyXml);
                string publicKeyXml = rsa.ToXmlString(false); // public only
                string publicKeyPath = Path.Combine(tempDirectory, $"public_{manv}.xml");
                File.WriteAllText(publicKeyPath, publicKeyXml);


                // Mã hóa
                byte[] encrypted = rsa.Encrypt(Encoding.UTF8.GetBytes(luong), false);

                // Output encrypted data as VARBINARY (byte array)
                string encryptedHex = BitConverter.ToString(encrypted).Replace("-", "");
                Console.WriteLine("Encrypted Salary: 0x" + encryptedHex);
            }
        }

        // 🔓 Hàm giải mã
        static void DecryptLuong(string manv, string mk, string encryptedHex)
        {
            string tempDirectory = @"D:\Temp";  // Match the directory used in EncryptLuong
            string privateKeyPath = Path.Combine(tempDirectory, $"private_{manv}_{mk}.xml");
            if (!File.Exists(privateKeyPath))
            {
                Console.WriteLine("Private key file not found at: " + privateKeyPath);
                return;
            }

            // Load private key
            string privateKeyXml = File.ReadAllText(privateKeyPath);
            using (RSACryptoServiceProvider rsa = new RSACryptoServiceProvider())
            {
                rsa.FromXmlString(privateKeyXml);

                try
                {
                    // Convert hex -> byte[]
                    byte[] encryptedBytes = HexToBytes(encryptedHex);
                    byte[] decryptedBytes = rsa.Decrypt(encryptedBytes, false);
                    string decryptedLuong = Encoding.UTF8.GetString(decryptedBytes);
                    Console.WriteLine("Decrypted Salary: " + decryptedLuong);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Decryption failed: " + ex.Message);
                }
            }
        }

        // Helper: Convert hex string to byte[]
        static byte[] HexToBytes(string hex)
        {
            int len = hex.Length / 2;
            byte[] bytes = new byte[len];
            for (int i = 0; i < len; i++)
                bytes[i] = Convert.ToByte(hex.Substring(i * 2, 2), 16);
            return bytes;
        }
    }
}
