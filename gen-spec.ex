ls = [
  "scala3",
  "alacritty",
  "zoxide",
  "nushell",
  "flameshot",
  "bottom",
  "wezterm",
  "exa",
  "dua-cli",
  "opam",
  "bat",
  "xplr"
]

for i <- ls do
  "https://raw.githubusercontent.com"
  |> URI.parse()
  |> URI.merge("topazus/fedora-copr/main/#{i}/#{i}.spec")
  |> to_string
  |> IO.puts()
end

IO.puts("\n")

for i <- ls do
  ("https://raw.githubusercontent.com" <> "topazus/fedora-copr/main/#{i}/#{i}.spec")
  |> IO.puts()
end
