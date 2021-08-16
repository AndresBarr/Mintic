package model.vo;

public class CompraPorProveedor {

    private Integer idCompra;
    private String proveedor;
    private String constructora;
    private String bancoVinculado;
    private String ciudad;

    public CompraPorProveedor() {

    }
    
    public CompraPorProveedor (Integer idCompra, String proveedor, String constructora, String bancoVinculado, String ciudad){

        this.idCompra = idCompra;
        this.proveedor = proveedor;
        this.constructora = constructora;
        this.bancoVinculado = bancoVinculado;
        this.ciudad = ciudad;
    }

    public Integer getIdCompra() {
        return idCompra;
    }

    public void setIdCompra(Integer idCompra) {
        this.idCompra = idCompra;
    }

    public String getProveedor() {
        return proveedor;
    }

    public void setProveedor (String proveedor) {
        this.proveedor = proveedor;
    }

    public String getConstructora() {
        return constructora;
    }

    public void setConstructora (String constructora) {
        this.constructora = constructora;
    }

    public String getBancoVinculado() {
        return bancoVinculado;
    }

    public void setBancoVinculado (String bancoVinculado) {
        this.bancoVinculado = bancoVinculado;
    }

    public String getCiudad() {
        return ciudad;
    }

    public void setCiudad (String ciudad) {
        this.ciudad = ciudad;
    }

}
