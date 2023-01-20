# SQLite voor logdata 

 * sqlitebiter: `pipx install sqlitebiter`
 * sqlite3 installeren: `sudo apt install sqlite3`
 * converteren csv/xlsx bestand: 
    ```bash
    sqlitebiter -o output.db file locust_output_2023-01-18_zonder_withsecure_1omgeving.csv 
    ```
## Sqlite3

```bash 
sqlite3 output.db "select * from data limit 10" 
```
output: 
```
2023-01-18 14:00:57.068157|0|0|0.0
2023-01-18 14:00:58.067871|0|0|0.0
2023-01-18 14:00:58.384307|0|0|0.0
2023-01-18 14:00:59.068071|70|98|0.0
2023-01-18 14:00:59.225213|70|98|0.0
2023-01-18 14:01:00.070246|70|98|0.0
2023-01-18 14:01:00.229438|70|98|0.0
2023-01-18 14:01:00.380118|70|98|0.0
2023-01-18 14:01:01.073465|57|98|1.0
2023-01-18 14:01:01.258746|57|98|1.0
```

```bash 
sqlite3 output.db "select * from data limit 10" -header -box
```
output: 
```
┌────────────────────────────┬────────────────────────┬────────────────────────┬───────────┐
│            date            │ median respone time 50 │ median respone time 95 │ total rps │
├────────────────────────────┼────────────────────────┼────────────────────────┼───────────┤
│ 2023-01-18 14:00:57.068157 │ 0                      │ 0                      │ 0.0       │
│ 2023-01-18 14:00:58.067871 │ 0                      │ 0                      │ 0.0       │
│ 2023-01-18 14:00:58.384307 │ 0                      │ 0                      │ 0.0       │
│ 2023-01-18 14:00:59.068071 │ 70                     │ 98                     │ 0.0       │
│ 2023-01-18 14:00:59.225213 │ 70                     │ 98                     │ 0.0       │
│ 2023-01-18 14:01:00.070246 │ 70                     │ 98                     │ 0.0       │
│ 2023-01-18 14:01:00.229438 │ 70                     │ 98                     │ 0.0       │
│ 2023-01-18 14:01:00.380118 │ 70                     │ 98                     │ 0.0       │
│ 2023-01-18 14:01:01.073465 │ 57                     │ 98                     │ 1.0       │
│ 2023-01-18 14:01:01.258746 │ 57                     │ 98                     │ 1.0       │
└────────────────────────────┴────────────────────────┴────────────────────────┴───────────┘

```

 * `.schema` - toont schema
 * `select * from tablename;` - toont alles van een tabel 
 * `select veld1, veld2 from tabel; `- selecteert 2 velden
 * ```sqlite
   select
   --     "median respone time 50",
   --        count("median respone time 50"),
          min("total rps"),
          max("total rps"),
          avg("total rps"),
          median("median respone time 50"),
          median("median respone time 95")
   from data
   -- group by "median respone time 50"
   ```
  * `select count(veld) from ... group by venster-clause ` - aantal keer dat 'veld' voorkomt
  * `select count(distinct veld) from ... group by venster-clause ` - aantal unieke waarden 
    binnen  'veld' dat voorkomt
